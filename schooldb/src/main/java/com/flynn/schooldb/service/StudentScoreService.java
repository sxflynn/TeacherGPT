package com.flynn.schooldb.service;

import com.flynn.schooldb.dto.CourseGradeDTO;
import com.flynn.schooldb.dto.ReportCardDTO;
import com.flynn.schooldb.entity.StudentScore;

import java.time.LocalDate;
import java.util.List;

public interface StudentScoreService {

    List<StudentScore> findByStudentId(Long studentId);

    List<StudentScore> findByStudentIdAndCourseName(Long studentId, String courseName);

    List<StudentScore> findByStudentIdAndCourseNameAndDateAssignedBetween(Long studentId, String courseName, LocalDate startDate, LocalDate endDate);

    List<StudentScore> findByStudentIdAndMissing(Long studentId, Integer limit);

    List<StudentScore> findByStudentIdAndPercentageScoreLessThan(Long studentId, Float scoreThreshold);

    List<StudentScore> findByCourseNameContainsAndDateAssignedBetween(String courseName, LocalDate startDate, LocalDate endDate);

    List<StudentScore> findByCourseNameContainsAndDateAssignedBetweenAndPercentageScoreLessThan(String courseName, LocalDate startDate, LocalDate endDate, Float threshold);

    List<StudentScore> findByCourseNameContainsAndDateAssignedBetweenAndMissingIsTrue(String courseName, LocalDate startDate, LocalDate endDate);

    CourseGradeDTO summarizeStudentCourseGradeBetweenDates(Long studentId, String courseName, LocalDate startDate, LocalDate endDate);

    ReportCardDTO summarizeAllStudentGrades(Long studentId, LocalDate startDate, LocalDate endDate);

    CourseGradeDTO summarizeWholeClassCourseGradeBetweenDates(String teacherLastName, String courseName, LocalDate startDate, LocalDate endDate);


}
