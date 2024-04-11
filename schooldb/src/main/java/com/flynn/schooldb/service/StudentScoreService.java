package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.StudentScore;
import org.springframework.data.domain.Limit;

import java.time.LocalDate;
import java.util.List;

public interface StudentScoreService {

    List<StudentScore> findByStudentId(Long studentId);

    List<StudentScore> findByStudentIdAndCourseName(Long studentId, String courseName);

    List<StudentScore> findByStudentIdAndCourseNameAndDateAssignedBetween(Long studentId, String courseName, LocalDate startDate, LocalDate endDate);

    List<StudentScore> findByStudentIdAndMissing(Long studentId, Limit limit);

    List<StudentScore> findByStudentIdAndPercentageScoreLessThan(Long studentId, Float scoreThreshold);

    List<StudentScore> findByCourseNameContainsAndDateAssignedBetween(String courseName, LocalDate startDate, LocalDate endDate);

    List<StudentScore> findByCourseNameContainsAndDateAssignedBetweenAndPercentageScoreLessThan(String courseName, LocalDate startDate, LocalDate endDate, Float threshold);

    List<StudentScore> findByCourseNameContainsAndDateAssignedBetweenAndMissingIsTrue(String courseName, LocalDate startDate, LocalDate endDate);


}
