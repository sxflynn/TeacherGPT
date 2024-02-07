package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.Student;
import com.flynn.schooldb.repository.StudentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;


import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@Service
public class StudentServiceImpl implements StudentService{

    private final StudentRepository studentRepository;

    @Autowired
    public StudentServiceImpl(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> getAllStudents() {
        return studentRepository.findAll();
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Student> getStudentById(Long id) {
        return studentRepository.findById(id);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> findByLastNameIgnoreCase(String lastName) {
        return studentRepository.findByLastNameIgnoreCase(lastName);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> findByFirstNameAndLastNameIgnoreCase(String firstName, String lastName) {
        return studentRepository.findByFirstNameIgnoreCaseAndLastNameIgnoreCase(firstName,lastName);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Student> findByEmail(String email) {
        return studentRepository.findByEmail(email);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> findByDob(LocalDate dob) {
        return studentRepository.findByDob(dob);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> findBySex(Character sex) {
        return studentRepository.findBySex(sex);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> findByDobBetween(LocalDate startDate, LocalDate endDate) {
        return studentRepository.findByDobBetween(startDate,endDate);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> findByLastNameOrderByFirstNameAsc(String lastName) {
        return studentRepository.findByLastNameOrderByFirstNameAsc(lastName);
    }

    @Override
    @Transactional(readOnly = true)
    public long countBySex(Character sex) {
        return studentRepository.countBySex(sex);
    }

    @Override
    @Transactional(readOnly = true)
    public boolean existsByEmail(String email) {
        return studentRepository.existsByEmail(email);
    }
}
