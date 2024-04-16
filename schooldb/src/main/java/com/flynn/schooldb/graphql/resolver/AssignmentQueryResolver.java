package com.flynn.schooldb.graphql.resolver;

import com.flynn.schooldb.entity.Assignment;
import com.flynn.schooldb.service.AssignmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.time.LocalDate;
import java.util.List;

@Controller
public class AssignmentQueryResolver {

    @Autowired
    AssignmentService assignmentService;

    @QueryMapping
    List<Assignment> assignmentsFindByCourseId(@Argument Long courseId){
        return assignmentService.findByCourseId(courseId);
    }
    @QueryMapping
    List<Assignment> assignmentsFindByStudentIdAndDateRange(@Argument Long studentId, @Argument LocalDate startDate, @Argument LocalDate endDate){
        return assignmentService.findByStudentIdAndDateRange(studentId,startDate,endDate);
    }
    @QueryMapping
    List<Assignment> assignmentsFindByTeacherIdAndDateRange(@Argument Long staffId, @Argument LocalDate startDate, @Argument LocalDate endDate){
        return assignmentService.findByTeacherIdAndDateRange(staffId,startDate,endDate);
    }
    @QueryMapping
    List<Assignment> assignmentsFindByCourseIdAndAssignmentType(@Argument Long courseId, @Argument String assignmentType){
        return assignmentService.findByCourseIdAndAssignmentType(courseId,assignmentType);
    }
    @QueryMapping
    List<Assignment> assignmentsFindByCourseIdAndDateAssignedBetweenAndAssignmentType(@Argument Long courseId, @Argument LocalDate startDate, @Argument LocalDate endDate, @Argument String assignmentType){
        return assignmentService.findByCourseIdAndDateAssignedBetweenAndAssignmentType(courseId,startDate,endDate,assignmentType);
    }

}
