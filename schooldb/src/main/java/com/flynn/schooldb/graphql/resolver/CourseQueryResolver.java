package com.flynn.schooldb.graphql.resolver;

import com.flynn.schooldb.entity.Course;
import com.flynn.schooldb.service.CourseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.util.Set;

@Controller
public class CourseQueryResolver {

    @Autowired
    CourseService courseService;

    @QueryMapping
    Set<Course> courseFindByCourseNameContains(@Argument String courseName){
        return courseService.findByCourseNameContains(courseName);
    }

    @QueryMapping
    Set<Course> courseFindByTeacherLastName(@Argument String lastName){
        return courseService.findByTeacherLastName(lastName);
    }

    @QueryMapping
    Set<Course> courseFindByGradeLevelName(@Argument String gradeLevelName){
        return courseService.findByGradeLevelName(gradeLevelName);
    }
    @QueryMapping
    Set<Course> courseFindByStudentId(@Argument Long studentId) {
        return courseService.findByStudentId(studentId);
    }
}
