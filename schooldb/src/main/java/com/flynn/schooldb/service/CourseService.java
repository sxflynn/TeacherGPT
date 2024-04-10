package com.flynn.schooldb.service;
import com.flynn.schooldb.entity.Course;

import java.util.List;
import java.util.Set;

public interface CourseService {

    List<Course> findAll();

    Set<Course> findByCourseNameContains(String courseName);

    Set<Course> findByTeacherLastName(String lastName);

    Set<Course> findByGradeLevelName(String gradeLevelName);

    Set<Course> findByStudentId(Long studentId);
}
