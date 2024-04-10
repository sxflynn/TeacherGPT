package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.Assignment;

import java.time.LocalDate;
import java.util.List;

public interface AssignmentService {

    List<Assignment> findByCourseId(Long courseId);

    List<Assignment> findByStudentIdAndDateRange(Long studentId, LocalDate startDate, LocalDate endDate);

    List<Assignment> findByTeacherIdAndDateRange(Long staffId, LocalDate startDate, LocalDate endDate);

    List<Assignment> findByCourseIdAndAssignmentType(Long courseId, String assignmentType);

    List<Assignment> findByCourseIdAndDateAssignedBetweenAndAssignmentType(Long courseId, LocalDate startDate, LocalDate endDate, String assignmentType);


}
