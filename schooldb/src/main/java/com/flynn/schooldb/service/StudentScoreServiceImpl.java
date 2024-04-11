package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.StudentScore;
import com.flynn.schooldb.repository.StudentScoreRepository;
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
}
