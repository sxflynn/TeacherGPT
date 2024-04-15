package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.Course;
import com.flynn.schooldb.repository.CourseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;
import java.util.Set;

@Service
public class CourseServiceImpl implements CourseService{

    private final CourseRepository courseRepository;

    @Autowired
    public CourseServiceImpl(CourseRepository courseRepository){
        this.courseRepository = courseRepository;
    }

    @Override
    public List<Course> findAll() {
        return courseRepository.findAll();
    }

    @Override
    @Transactional(readOnly = true)
    public Set<Course> findByCourseNameContains(String courseName) {
        return courseRepository.findByCourseNameContainsIgnoreCase(courseName);
    }

    @Override
    @Transactional(readOnly = true)
    public Set<Course> findByTeacherLastName(String lastName) {
        return courseRepository.findByLeadTeacherLastNameContainsIgnoreCase(lastName);
    }

    @Override
    public Set<Course> findByTeacherLastNameContainsAndCourseNameContains(String lastName, String courseName) {
        return courseRepository.findByLeadTeacherLastNameContainsIgnoreCaseAndCourseNameContainsIgnoreCase(lastName,courseName);
    }

    @Override
    @Transactional(readOnly = true)
    public Set<Course> findByGradeLevelName(String gradeLevelName) {
        return courseRepository.findByGradeLevelGradeLevelNameContainsIgnoreCase(gradeLevelName);
    }

    @Override
    @Transactional(readOnly = true)
    public Set<Course> findByStudentId(Long studentId) {
        return courseRepository.findByStudentsStudentId(studentId);
    }

    @Override
    public Optional<Course> findByStudentIdAndCourseNameContains(Long studentId, String courseName) {
        return courseRepository.findByStudentsStudentIdAndCourseNameContainsIgnoreCase(studentId,courseName);
    }

}
