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
    public List<Student> studentsListAll(){
        return studentRepository.findAll();
    }
    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByFirstNameIgnoreCase(String firstName) {
        return studentRepository.findByFirstNameIgnoreCase(firstName);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByLastNameIgnoreCase(String lastName) {
        return studentRepository.findByLastNameIgnoreCase(lastName);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByFirstNameStartingWith(String firstLetter){
        return studentRepository.findByFirstNameStartingWith(firstLetter);
    }
    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByLastNameStartingWith(String firstLetter){
        return studentRepository.findByLastNameStartingWith(firstLetter);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByMiddleNameIgnoreCase(String middleName) {
        return studentRepository.findByMiddleNameIgnoreCase(middleName);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByFirstNameIgnoreCaseAndLastNameIgnoreCase(String firstName, String lastName) {
        return studentRepository.findByFirstNameIgnoreCaseAndLastNameIgnoreCase(firstName,lastName);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByFirstNameIgnoreCaseOrMiddleNameIgnoreCaseOrLastNameIgnoreCase(String firstName, String middleName, String lastName) {
        return studentRepository.findByFirstNameIgnoreCaseOrMiddleNameIgnoreCaseOrLastNameIgnoreCase(firstName,middleName,lastName);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsSearchByKeyword(String keyword) {
        return studentRepository.searchByKeyword(keyword);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Student> studentsFindByEmail(String email) {
        return studentRepository.findByEmail(email);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByBirthMonth(int month) {
        return studentRepository.findByBirthMonth(month);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByDob(LocalDate dob) {
        return studentRepository.findByDob(dob);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByDobBefore(LocalDate date) {
        return studentRepository.findByDobBefore(date);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByDobAfter(LocalDate date) {
        return studentRepository.findByDobAfter(date);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindBySex(Character sex) {
        return studentRepository.findBySex(sex);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByDobBetween(LocalDate startDate, LocalDate endDate) {
        return studentRepository.findByDobBetween(startDate,endDate);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByLastNameOrderByFirstNameAsc(String lastName) {
        return studentRepository.findByLastNameOrderByFirstNameAsc(lastName);
    }

    @Override
    @Transactional(readOnly = true)
    public long studentsCountBySex(Character sex) {
        return studentRepository.countBySex(sex);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindBySexOrderByLastNameAsc(Character sex) {
        return studentRepository.findBySexOrderByLastNameAsc(sex);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Student> studentsFindByEmailContainingIgnoreCase(String emailFragment) {
        return studentRepository.findByEmailContainingIgnoreCase(emailFragment);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Student> studentFindById(Long id) {
        return studentRepository.findById(id);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Student> studentsFindByOhioSsid(String ohioSsid) {
        return studentRepository.findByOhioSsid(ohioSsid);
    }
}
