package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.Course;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Set;

public interface CourseRepository extends JpaRepository<Course, Long> {

    Set<Course> findByCourseNameContainsIgnoreCase(String courseName);

    Set<Course> findByLeadTeacherLastNameContainsIgnoreCase(String leadTeacher);

    Set<Course> findByGradeLevelGradeLevelNameContainsIgnoreCase(String gradeLevelName);

    Set<Course> findByStudentsStudentId(Long studentId);

}
