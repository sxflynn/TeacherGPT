package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.Assignment;
import com.flynn.schooldb.repository.AssignmentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.List;

@Service
public class AssignmentServiceImpl implements AssignmentService {

    private final AssignmentRepository assignmentRepository;

    @Autowired
    public AssignmentServiceImpl(AssignmentRepository assignmentRepository){
        this.assignmentRepository = assignmentRepository;
    }

    @Override
    @Transactional(readOnly = true)
    public List<Assignment> findByCourseId(Long courseId) {
        return assignmentRepository.findByCourseCourseId(courseId);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Assignment> findByStudentIdAndDateRange(Long studentId, LocalDate startDate, LocalDate endDate) {
        return assignmentRepository.findByCourseStudentsStudentIdAndDateAssignedBetween(studentId,startDate,endDate);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Assignment> findByTeacherIdAndDateRange(Long staffId, LocalDate startDate, LocalDate endDate) {
        return assignmentRepository.findByCourseLeadTeacherStaffIdAndDateAssignedBetween(staffId,startDate,endDate);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Assignment> findByCourseIdAndAssignmentType(Long courseId, String assignmentType) {
        String validatedAssignmentType = findValidAssignmentTypeOrDefault(assignmentType);
        return assignmentRepository.findByCourseCourseIdAndAssignmentTypeContainsIgnoreCase(courseId,validatedAssignmentType);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Assignment> findByCourseIdAndDateAssignedBetweenAndAssignmentType(Long courseId, LocalDate startDate, LocalDate endDate, String assignmentType) {
        String validatedAssignmentType = findValidAssignmentTypeOrDefault(assignmentType);
        return assignmentRepository.findByCourseCourseIdAndDateAssignedBetweenAndAssignmentTypeContainsIgnoreCase(courseId,startDate,endDate,validatedAssignmentType);
    }

    private static final List<String> VALID_ASSIGNMENT_TYPES = Arrays.asList(
            "Unit Test", "Quiz", "Essay", "Homework"
    );

    public static String findValidAssignmentTypeOrDefault(String assignmentType) {
        for (String validType : VALID_ASSIGNMENT_TYPES) {
            if (validType.toLowerCase().contains(assignmentType.toLowerCase())) {
                return validType;
            }
        }
        return "Homework";
    }
}




