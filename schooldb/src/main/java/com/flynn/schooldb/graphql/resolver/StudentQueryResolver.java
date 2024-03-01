package com.flynn.schooldb.graphql.resolver;
import com.flynn.schooldb.entity.Student;
import com.flynn.schooldb.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@Controller
public class StudentQueryResolver {
    @Autowired
    private StudentService studentService;

    @QueryMapping
    List<Student> studentsListAll(){
        return studentService.studentsListAll();
    }
    @QueryMapping
    Optional<Student> studentsFindById(@Argument Long id){
        return studentService.studentFindById(id);
    }
    @QueryMapping
    Optional<Student> studentsFindByOhioSsid(@Argument String ohioSsid){
        return studentService.studentsFindByOhioSsid(ohioSsid);
    }
    @QueryMapping
    List<Student> studentsFindByFirstNameIgnoreCase(@Argument String firstName){
        return studentService.studentsFindByFirstNameIgnoreCase(firstName);
    }
    @QueryMapping
    public List<Student> studentsFindByLastNameIgnoreCase(@Argument String lastName){
        return studentService.studentsFindByLastNameIgnoreCase(lastName);
    }
    @QueryMapping
    public List<Student> studentsFindByMiddleNameIgnoreCase(@Argument String middleName){
        return studentService.studentsFindByMiddleNameIgnoreCase(middleName);
    }
    @QueryMapping
    public List<Student> studentsFindByFirstNameIgnoreCaseAndLastNameIgnoreCase(@Argument String firstName, @Argument String lastName){
        return studentService.studentsFindByFirstNameIgnoreCaseAndLastNameIgnoreCase(firstName, lastName);
    }
    @QueryMapping
    public List<Student> studentsFindByFirstNameIgnoreCaseOrMiddleNameIgnoreCaseOrLastNameIgnoreCase(@Argument String firstName, @Argument String middleName, @Argument String lastName){
        return studentService.studentsFindByFirstNameIgnoreCaseOrMiddleNameIgnoreCaseOrLastNameIgnoreCase(firstName, middleName, lastName);
    }
    @QueryMapping
    public List<Student> studentsSearchByKeyword(@Argument String keyword){
        return studentService.studentsSearchByKeyword(keyword);
    }
    @QueryMapping
    public Optional<Student> studentsFindByEmail(@Argument String email){
        return studentService.studentsFindByEmail(email);
    }

    @QueryMapping
    public List<Student> studentsFindByBirthMonth(@Argument int month){
        return studentService.studentsFindByBirthMonth(month);
    }

    @QueryMapping
    public List<Student> studentsFindByDob(@Argument LocalDate dob){
        return studentService.studentsFindByDob(dob);
    }
    @QueryMapping
    public List<Student> studentsFindByDobBefore(@Argument LocalDate date){
        return studentService.studentsFindByDobBefore(date);
    }
    @QueryMapping
    public List<Student> studentsFindByDobAfter(@Argument LocalDate date){
        return studentService.studentsFindByDobAfter(date);
    }
    @QueryMapping
    public List<Student> studentsFindBySex(@Argument Character sex){
        return studentService.studentsFindBySex(sex);
    }
    @QueryMapping
    public List<Student> studentsFindByDobBetween(@Argument LocalDate startDate, @Argument LocalDate endDate){
        return studentService.studentsFindByDobBetween(startDate, endDate);
    }
    @QueryMapping
    public List<Student> studentsFindByLastNameOrderByFirstNameAsc(@Argument String lastName){
        return studentService.studentsFindByLastNameOrderByFirstNameAsc(lastName);
    }
    @QueryMapping
    public long studentsCountBySex(@Argument Character sex){
        return studentService.studentsCountBySex(sex);
    }
    @QueryMapping
    public List<Student> studentsFindBySexOrderByLastNameAsc(@Argument Character sex){
        return studentService.studentsFindBySexOrderByLastNameAsc(sex);
    }
    @QueryMapping
    public List<Student> studentsFindByEmailContainingIgnoreCase(@Argument String emailFragment){
        return studentService.studentsFindByEmailContainingIgnoreCase(emailFragment);
    }
}



