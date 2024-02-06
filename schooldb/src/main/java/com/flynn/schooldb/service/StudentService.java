package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.Student;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

public interface StudentService {
    Student saveStudent(Student student);

    List<Student> getAllStudents();

    Optional<Student> getStudentById(Long id);

    Student updateStudent(Long id, Student studentDetails);

    void deleteStudent(Long id);

    List<Student> findByLastNameIgnoreCase(String lastName);

    List<Student> findByFirstNameAndLastNameIgnoreCase(String firstName, String lastName);

    Optional<Student> findByEmail(String email);

    List<Student> findByDob(LocalDate dob);

    List<Student> findBySex(Character sex);

    List<Student> findByDobBetween(LocalDate startDate, LocalDate endDate);

    List<Student> findByLastNameOrderByFirstNameAsc(String lastName);

    long countBySex(Character sex);

    boolean existsByEmail(String email);
}