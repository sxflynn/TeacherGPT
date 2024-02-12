package com.flynn.schooldb.graphql.resolver;
import com.flynn.schooldb.entity.Student;
import com.flynn.schooldb.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.util.List;
import java.util.Optional;

@Controller
public class StudentQueryResolver {
    @Autowired
    private StudentService studentService;

    @QueryMapping
    public Optional<Student> studentById(@Argument Long id) {
        return studentService.getStudentById(id);
    }

    @QueryMapping
    public List<Student> allStudents() {
        return studentService.getAllStudents();
    }

    @QueryMapping
    public List<Student> studentsByLastName(@Argument String lastName){
        return studentService.findByLastNameIgnoreCase(lastName);
    }
}



