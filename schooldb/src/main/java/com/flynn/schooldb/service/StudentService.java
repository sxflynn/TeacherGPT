package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.Student;
import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

public interface StudentService {
    List<Student> studentsListAll();
    Optional<Student> studentFindById(Long id);
    Optional<Student> studentsFindByOhioSsid(String ohioSsid);
    List<Student> studentsFindByFirstNameIgnoreCase(String firstName);
    List<Student> studentsFindByLastNameIgnoreCase(String lastName);
    List<Student> studentsFindByMiddleNameIgnoreCase(String middleName);
    List<Student> studentsFindByFirstNameIgnoreCaseAndLastNameIgnoreCase(String firstName, String lastName);
    List<Student> studentsFindByFirstNameIgnoreCaseOrMiddleNameIgnoreCaseOrLastNameIgnoreCase(String firstName, String middleName, String lastName);
    List<Student> studentsSearchByKeyword(String keyword);
    Optional<Student> studentsFindByEmail(String email);
    List<Student> studentsFindByBirthMonth(int month);
    List<Student> studentsFindByDob(LocalDate dob);
    List<Student> studentsFindByDobBefore(LocalDate date);
    List<Student> studentsFindByDobAfter(LocalDate date);
    List<Student> studentsFindBySex(Character sex);
    List<Student> studentsFindByDobBetween(LocalDate startDate, LocalDate endDate);
    List<Student> studentsFindByLastNameOrderByFirstNameAsc(String lastName);
    long studentsCountBySex(Character sex);
    List<Student> studentsFindBySexOrderByLastNameAsc(Character sex);
    List<Student> studentsFindByEmailContainingIgnoreCase(String emailFragment);

}