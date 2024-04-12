package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.StudentScore;
import com.flynn.schooldb.entity.StudentScoreId;
import org.springframework.data.domain.Limit;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.time.LocalDate;
import java.util.List;

public interface StudentScoreRepository extends JpaRepository<StudentScore, StudentScoreId> {

    // List all scores, not optimal
    List<StudentScore> findByStudentStudentIdOrderByAssignmentDateAssignedDesc(Long studentId);

    List<StudentScore> findByStudentStudentIdAndAssignmentCourseCourseNameContainsIgnoreCaseOrderByAssignmentDateAssignedDesc(Long studentId, String courseName);

    List<StudentScore> findByStudentStudentIdAndAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenOrderByAssignmentDateAssignedDesc(Long studentId, String courseName, LocalDate startDate, LocalDate endDate);

    List<StudentScore> findByStudentStudentIdAndMissingIsTrueOrderByAssignmentDateAssignedDesc(Long studentId, Limit limit);

    List<StudentScore> findByStudentStudentIdAndPercentageScoreLessThan(Long studentId, Float threshold);

    List<StudentScore> findByAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenOrderByAssignmentDateAssignedDesc(String courseName, LocalDate startDate, LocalDate endDate);

    List<StudentScore> findByAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenAndPercentageScoreLessThanOrderByAssignmentDateAssignedDesc(String courseName, LocalDate startDate, LocalDate endDate, Float threshold);

    List<StudentScore> findByAssignmentCourseCourseNameContainsIgnoreCaseAndAssignmentDateAssignedBetweenAndMissingIsTrueOrderByAssignmentDateAssignedDesc(String courseName, LocalDate startDate, LocalDate endDate);


    // CourseGradeDTO repository methods

    // count all grades between dates
    @Query("SELECT COUNT(ss) FROM StudentScore ss WHERE ss.student.studentId = :studentId AND LOWER(ss.assignment.course.courseName) LIKE LOWER(CONCAT('%', :courseName, '%')) AND ss.assignment.dateAssigned BETWEEN :startDate AND :endDate")
    Long countByStudentIdAndCourseNameLikeAndDateAssignedBetween(Long studentId, String courseName, LocalDate startDate, LocalDate endDate);

    // sum the points earned
    @Query("SELECT SUM(ss.pointsEarned) FROM StudentScore ss WHERE ss.student.studentId = :studentId AND LOWER(ss.assignment.course.courseName) LIKE LOWER(CONCAT('%', :courseName, '%')) AND ss.assignment.dateAssigned BETWEEN :startDate AND :endDate")
    Long sumPointsEarnedByStudentAndCourseBetweenDates(Long studentId, String courseName, LocalDate startDate, LocalDate endDate);

    // sum the total values
    @Query("SELECT SUM(ss.assignment.assignmentValue) FROM StudentScore ss WHERE ss.student.studentId = :studentId AND LOWER(ss.assignment.course.courseName) LIKE LOWER(CONCAT('%', :courseName, '%')) AND ss.assignment.dateAssigned BETWEEN :startDate AND :endDate")
    Long sumAssignmentValueByStudentAndCourseBetweenDates(Long studentId, String courseName, LocalDate startDate, LocalDate endDate);

}
