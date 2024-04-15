package com.flynn.schooldb.service;
import com.flynn.schooldb.entity.Course;

import java.util.List;
import java.util.Optional;
import java.util.Set;

public interface CourseService {

    List<Course> findAll();

    Set<Course> findByCourseNameContains(String courseName);

    Set<Course> findByTeacherLastName(String lastName);

    Set<Course> findByTeacherLastNameContainsAndCourseNameContains(String lastName, String courseName);

    Set<Course> findByGradeLevelName(String gradeLevelName);

    Set<Course> findByStudentId(Long studentId);

    Optional<Course> findByStudentIdAndCourseNameContains(Long studentId, String courseName);
}
