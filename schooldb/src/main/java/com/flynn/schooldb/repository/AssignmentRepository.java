package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.Assignment;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDate;
import java.util.List;

public interface AssignmentRepository extends JpaRepository<Assignment,Long> {

    List<Assignment> findByCourseCourseId(Long courseId);

    List<Assignment> findByCourseStudentsStudentIdAndDateAssignedBetween(Long studentId, LocalDate startDate, LocalDate endDate);

    List<Assignment> findByCourseLeadTeacherStaffIdAndDateAssignedBetween(Long staffId, LocalDate startDate, LocalDate endDate);

    List<Assignment> findByCourseCourseIdAndAssignmentTypeContainsIgnoreCase(Long courseId, String assignmentType);

    List<Assignment> findByCourseCourseIdAndDateAssignedBetweenAndAssignmentTypeContainsIgnoreCase(Long courseId, LocalDate startDate, LocalDate endDate, String assignmentType);

}
