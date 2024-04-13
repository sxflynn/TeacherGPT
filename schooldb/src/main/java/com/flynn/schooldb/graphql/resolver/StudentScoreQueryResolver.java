package com.flynn.schooldb.graphql.resolver;

import com.flynn.schooldb.dto.CourseGradeDTO;
import com.flynn.schooldb.entity.StudentScore;
import com.flynn.schooldb.service.StudentScoreService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.time.LocalDate;
import java.util.List;

@Controller
public class StudentScoreQueryResolver {

    @Autowired
    private StudentScoreService studentScoreService;

    @QueryMapping
    public List<StudentScore> findByStudentId(@Argument Long studentId) {
        return studentScoreService.findByStudentId(studentId);
    }

    @QueryMapping
    public List<StudentScore> studentScoreFindByStudentIdAndCourseName(@Argument Long studentId, @Argument String courseName) {
        return studentScoreService.findByStudentIdAndCourseName(studentId,courseName);
    }

    @QueryMapping
    public List<StudentScore> studentScoreFindByStudentIdAndCourseNameAndDateAssignedBetween(@Argument Long studentId, @Argument String courseName, @Argument LocalDate startDate, @Argument LocalDate endDate) {
        return studentScoreService.findByStudentIdAndCourseNameAndDateAssignedBetween(studentId,courseName,startDate,endDate);
    }

    @QueryMapping
    public List<StudentScore> studentScoreFindByStudentIdAndMissing(@Argument Long studentId, @Argument Integer limit) {
        return studentScoreService.findByStudentIdAndMissing(studentId, limit);
    }

    @QueryMapping
    public List<StudentScore> studentScoreFindByStudentIdAndPercentageScoreLessThan(@Argument Long studentId, @Argument Float scoreThreshold) {
        return studentScoreService.findByStudentIdAndPercentageScoreLessThan(studentId,scoreThreshold);
    }

    @QueryMapping
    public List<StudentScore> studentScoreFindByCourseNameContainsAndDateAssignedBetween(@Argument String courseName, @Argument LocalDate startDate, @Argument LocalDate endDate) {
        return studentScoreService.findByCourseNameContainsAndDateAssignedBetween(courseName,startDate,endDate);
    }

    @QueryMapping
    public List<StudentScore> studentScoreFindByCourseNameContainsAndDateAssignedBetweenAndPercentageScoreLessThan(@Argument String courseName, @Argument LocalDate startDate,@Argument  LocalDate endDate, @Argument Float threshold) {
        return studentScoreService.findByCourseNameContainsAndDateAssignedBetweenAndPercentageScoreLessThan(courseName,startDate,endDate,threshold);
    }

    @QueryMapping
    public List<StudentScore> studentScoreFindByCourseNameContainsAndDateAssignedBetweenAndMissingIsTrue(@Argument String courseName, @Argument LocalDate startDate,@Argument LocalDate endDate) {
        return studentScoreService.findByCourseNameContainsAndDateAssignedBetweenAndMissingIsTrue(courseName,startDate,endDate);
    }

    @QueryMapping
    public CourseGradeDTO summarizeStudentCourseGradeBetweenDates(@Argument Long studentId, @Argument String courseName, @Argument LocalDate startDate, @Argument LocalDate endDate) {
        return studentScoreService.summarizeStudentCourseGradeBetweenDates(studentId,courseName,startDate,endDate);
    }

    @QueryMapping
    public CourseGradeDTO summarizeWholeClassCourseGradeBetweenDates(@Argument String teacherLastName, @Argument String courseName, @Argument LocalDate startDate, @Argument LocalDate endDate) {
        return studentScoreService.summarizeWholeClassCourseGradeBetweenDates(teacherLastName,courseName,startDate,endDate);
    }

}
