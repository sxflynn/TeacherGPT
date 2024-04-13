package com.flynn.schooldb.service;

import com.flynn.schooldb.dto.CourseGradeDTO;
import com.flynn.schooldb.entity.StudentScore;
import com.flynn.schooldb.repository.StudentScoreRepository;
import com.flynn.schooldb.util.LetterGrade;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Limit;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.List;

@Service
public class StudentScoreServiceImpl implements StudentScoreService {

    private final StudentScoreRepository studentScoreRepository;
    
    @Autowired
    public StudentScoreServiceImpl(StudentScoreRepository studentScoreRepository) {
        this.studentScoreRepository = studentScoreRepository;
    }

    @Override
    public List<StudentScore> findByStudentId(Long studentId) {
        return studentScoreRepository.findByStudentStudentIdOrderByAssignmentDateAssignedDesc(studentId);
    }

    @Override
    public List<StudentScore> findByStudentIdAndCourseName(Long studentId, String courseName) {
        return studentScoreRepository.findByStudentStudentIdAndAssignmentCourseCourseNameContainsIgnoreCaseOrderByAssignmentDateAssignedDesc(studentId,courseName);
    }

    @Override
    public List<StudentScore> findByStudentIdAndCourseNameAndDateAssignedBetween(Long studentId, String courseName, LocalDate startDate, LocalDate endDate) {
        return studentScoreRepository.findByStudentStudentIdAndAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenOrderByAssignmentDateAssignedDesc(studentId,courseName,startDate,endDate);
    }

    @Override
    public List<StudentScore> findByStudentIdAndMissing(Long studentId, Integer limit) {
        return studentScoreRepository.findByStudentStudentIdAndMissingIsTrueOrderByAssignmentDateAssignedDesc(studentId,Limit.of(limit));
    }

    @Override
    public List<StudentScore> findByStudentIdAndPercentageScoreLessThan(Long studentId, Float scoreThreshold) {
        return studentScoreRepository.findByStudentStudentIdAndPercentageScoreLessThan(studentId,scoreThreshold);
    }

    @Override
    public List<StudentScore> findByCourseNameContainsAndDateAssignedBetween(String courseName, LocalDate startDate, LocalDate endDate) {
        return studentScoreRepository.findByAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenOrderByAssignmentDateAssignedDesc(courseName,startDate,endDate);
    }

    @Override
    public List<StudentScore> findByCourseNameContainsAndDateAssignedBetweenAndPercentageScoreLessThan(String courseName, LocalDate startDate, LocalDate endDate, Float threshold) {
        return studentScoreRepository.findByAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenAndPercentageScoreLessThanOrderByAssignmentDateAssignedDesc(courseName,startDate,endDate,threshold);
    }

    @Override
    public List<StudentScore> findByCourseNameContainsAndDateAssignedBetweenAndMissingIsTrue(String courseName, LocalDate startDate, LocalDate endDate) {
        return studentScoreRepository.findByAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenAndMissingIsTrueOrderByAssignmentDateAssignedDesc(courseName,startDate,endDate);
    }

    @Override
    public CourseGradeDTO summarizeStudentCourseGradeBetweenDates(Long studentId, String courseName, LocalDate startDate, LocalDate endDate) {

        Integer numberOfAssignments = studentScoreRepository.countByStudentIdAndCourseNameLikeAndDateAssignedBetween(studentId,courseName,startDate,endDate);
        Integer totalAssignmentValues = studentScoreRepository.sumAssignmentValueByStudentAndCourseBetweenDates(studentId,courseName,startDate,endDate);
        Integer totalPointsEarned = studentScoreRepository.sumPointsEarnedByStudentAndCourseBetweenDates(studentId,courseName,startDate,endDate);

        Float averageScore = Float.valueOf((float) totalPointsEarned /totalAssignmentValues);
        int scoreForLetterGrade = (int) (averageScore * 100);
        String letterGrade = LetterGrade.toLetterGrade(scoreForLetterGrade);

        CourseGradeDTO summary = new CourseGradeDTO(
                studentId,
                courseName,
                startDate,
                endDate,
                numberOfAssignments,
                averageScore,
                letterGrade
        );

        return summary;
    }

    @Override
    public CourseGradeDTO summarizeWholeClassCourseGradeBetweenDates(String teacherLastName, String courseName, LocalDate startDate, LocalDate endDate) {

        Integer numberOfAssignments = studentScoreRepository.countByCourseNameLikeAndDateAssignedBetweenDates(courseName,teacherLastName,startDate,endDate);
        Integer totalAssignmentValues = studentScoreRepository.sumAssignmentValueByCourseAndTeacherBetweenDates(courseName,teacherLastName,startDate,endDate);
        Integer totalPointsEarned = studentScoreRepository.sumPointsEarnedByCourseAndTeacherBetweenDates(courseName,teacherLastName,startDate,endDate);

        Float averageScore = Float.valueOf((float) totalPointsEarned /totalAssignmentValues);
        int scoreForLetterGrade = (int) (averageScore * 100);
        String letterGrade = LetterGrade.toLetterGrade(scoreForLetterGrade);


        CourseGradeDTO summary = new CourseGradeDTO(
                teacherLastName,
                courseName,
                startDate,
                endDate,
                numberOfAssignments,
                averageScore,
                letterGrade
        );

        return summary;
    }
}
