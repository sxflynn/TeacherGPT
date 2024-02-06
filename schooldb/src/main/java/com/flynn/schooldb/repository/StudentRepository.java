package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.Student;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.awt.print.Pageable;
import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {
    List<Student> findByLastNameIgnoreCase(String lastName);
    List<Student> findByFirstNameIgnoreCaseAndLastNameIgnoreCase(String firstName, String lastName);
    Optional<Student> findByEmail(String email);
    List<Student> findByDob(LocalDate dob);
    List<Student> findBySex(Character sex);
    List<Student> findByDobBetween(LocalDate startDate, LocalDate endDate);
    List<Student> findByLastNameOrderByFirstNameAsc(String lastName);
    long countBySex(Character sex);
    boolean existsByEmail(String email);
}
