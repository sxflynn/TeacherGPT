package com.flynn.schooldb.service;

import com.flynn.schooldb.dto.CourseGradeDTO;
import com.flynn.schooldb.dto.ReportCardDTO;
import com.flynn.schooldb.entity.Course;
import com.flynn.schooldb.entity.Student;
import com.flynn.schooldb.entity.StudentScore;
import com.flynn.schooldb.repository.StudentScoreRepository;
import com.flynn.schooldb.util.GradeCalculator;
import com.flynn.schooldb.util.LetterGrade;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Limit;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.util.*;

@Service
public class StudentScoreServiceImpl implements StudentScoreService {

    private final StudentScoreRepository studentScoreRepository;
    private final CourseService courseService;
    private final StudentService studentService;
    private final StaffService staffService;
    
    @Autowired
    public StudentScoreServiceImpl(StudentScoreRepository studentScoreRepository, CourseService courseService, StudentService studentService, StaffService staffService) {
        this.studentScoreRepository = studentScoreRepository;
        this.courseService = courseService;
        this.studentService = studentService;
        this.staffService = staffService;
    }

    @Override
    @Transactional(readOnly = true)
    public List<StudentScore> findByStudentId(Long studentId) {
        return studentScoreRepository.findByStudentStudentIdOrderByAssignmentDateAssignedDesc(studentId);
    }

    @Override
    @Transactional(readOnly = true)
    public List<StudentScore> findByStudentIdAndCourseName(Long studentId, String courseName) {
        return studentScoreRepository.findByStudentStudentIdAndAssignmentCourseCourseNameContainsIgnoreCaseOrderByAssignmentDateAssignedDesc(studentId,courseName);
    }

    @Override
    @Transactional(readOnly = true)
    public List<StudentScore> findByStudentIdAndCourseNameAndDateAssignedBetween(Long studentId, String courseName, LocalDate startDate, LocalDate endDate) {
        return studentScoreRepository.findByStudentStudentIdAndAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenOrderByAssignmentDateAssignedDesc(studentId,courseName,startDate,endDate);
    }

    @Override
    @Transactional(readOnly = true)
    public List<StudentScore> findByStudentIdAndMissing(Long studentId, Integer limit) {
        return studentScoreRepository.findByStudentStudentIdAndMissingIsTrueOrderByAssignmentDateAssignedDesc(studentId,Limit.of(limit));
    }

    @Override
    @Transactional(readOnly = true)
    public List<StudentScore> findByStudentIdAndPercentageScoreLessThan(Long studentId, Float scoreThreshold) {
        return studentScoreRepository.findByStudentStudentIdAndPercentageScoreLessThan(studentId,scoreThreshold);
    }

    @Override
    @Transactional(readOnly = true)
    public List<StudentScore> findByCourseNameContainsAndDateAssignedBetween(String courseName, LocalDate startDate, LocalDate endDate) {
        return studentScoreRepository.findByAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenOrderByAssignmentDateAssignedDesc(courseName,startDate,endDate);
    }

    @Override
    @Transactional(readOnly = true)
    public List<StudentScore> findByCourseNameContainsAndDateAssignedBetweenAndPercentageScoreLessThan(String courseName, LocalDate startDate, LocalDate endDate, Float threshold) {
        return studentScoreRepository.findByAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenAndPercentageScoreLessThanOrderByAssignmentDateAssignedDesc(courseName,startDate,endDate,threshold);
    }

    @Override
    @Transactional(readOnly = true)
    public List<StudentScore> findByCourseNameContainsAndDateAssignedBetweenAndMissingIsTrue(String courseName, LocalDate startDate, LocalDate endDate) {
        return studentScoreRepository.findByAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenAndMissingIsTrueOrderByAssignmentDateAssignedDesc(courseName,startDate,endDate);
    }

    @Override
    @Transactional(readOnly = true)
    public CourseGradeDTO summarizeStudentCourseGradeBetweenDates(Long studentId, String courseName, LocalDate startDate, LocalDate endDate) {

        Optional<Student> student = studentService.studentFindById(studentId);
        Optional<Course> course = courseService.findByStudentIdAndCourseNameContains(studentId,courseName);
        Integer numberOfAssignments = studentScoreRepository.countByStudentIdAndCourseNameLikeAndDateAssignedBetween(studentId,courseName,startDate,endDate);
        Integer totalAssignmentValues = studentScoreRepository.sumAssignmentValueByStudentAndCourseBetweenDates(studentId,courseName,startDate,endDate);
        Integer totalPointsEarned = studentScoreRepository.sumPointsEarnedByStudentAndCourseBetweenDates(studentId,courseName,startDate,endDate);

        Float averageScore = Float.valueOf((float) totalPointsEarned /totalAssignmentValues);
        int scoreForLetterGrade = (int) (averageScore * 100);
        String letterGrade = LetterGrade.toLetterGrade(scoreForLetterGrade);

        CourseGradeDTO summary = new CourseGradeDTO(
                student,
                course,
                startDate,
                endDate,
                numberOfAssignments,
                averageScore,
                letterGrade
        );

        return summary;
    }

    @Override
    @Transactional(readOnly = true)
    public ReportCardDTO summarizeAllStudentGrades(Long studentId, LocalDate startDate, LocalDate endDate) {

        Optional<Student> student = studentService.studentFindById(studentId);
        Set<Course> allCourses = courseService.findByStudentId(studentId);
        if (allCourses.isEmpty()) {
            throw new NoSuchElementException("No courses found for student ID: " + studentId);
        }
        List<CourseGradeDTO> allGradeSummaries = new ArrayList<>();
        for (Course course:allCourses){
            CourseGradeDTO courseSummary = summarizeStudentCourseGradeBetweenDates(studentId,course.getCourseName(),startDate,endDate);
            allGradeSummaries.add(courseSummary);
        }

        if (allGradeSummaries.isEmpty()) {
            throw new IllegalStateException("Failed to generate any course summaries for student ID: " + studentId);
        }

        Float gradeAverage = GradeCalculator.calculateGradeAverage(allGradeSummaries);

        ReportCardDTO reportCard = new ReportCardDTO(
                student,
                allGradeSummaries,
                gradeAverage,
                startDate,
                endDate
        );
        return reportCard;
    }

    @Override
    @Transactional(readOnly = true)
    public CourseGradeDTO summarizeWholeClassCourseGradeBetweenDates(String teacherLastName, String courseName, LocalDate startDate, LocalDate endDate) {

        Set<Course> courses = courseService.findByTeacherLastNameContainsAndCourseNameContains(teacherLastName,courseName);
        Optional<Course> course = courses.stream().findFirst();
        Integer numberOfAssignments = studentScoreRepository.countByCourseNameLikeAndDateAssignedBetweenDates(courseName,teacherLastName,startDate,endDate);
        Integer totalAssignmentValues = studentScoreRepository.sumAssignmentValueByCourseAndTeacherBetweenDates(courseName,teacherLastName,startDate,endDate);
        Integer totalPointsEarned = studentScoreRepository.sumPointsEarnedByCourseAndTeacherBetweenDates(courseName,teacherLastName,startDate,endDate);

        if (totalAssignmentValues == 0) {
            return null;
        }


        Float averageScore = Float.valueOf((float) totalPointsEarned /totalAssignmentValues);
        int scoreForLetterGrade = (int) (averageScore * 100);
        String letterGrade = LetterGrade.toLetterGrade(scoreForLetterGrade);


        CourseGradeDTO summary = new CourseGradeDTO(
                course,
                startDate,
                endDate,
                numberOfAssignments,
                averageScore,
                letterGrade
        );

        return summary;
    }
}
