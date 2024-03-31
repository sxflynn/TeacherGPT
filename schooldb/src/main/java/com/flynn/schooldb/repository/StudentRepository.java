package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.Student;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {

    List<Student> findAll();

    Optional<Student> findByOhioSsid(String ohioSsid);

    List<Student> findByFirstNameIgnoreCase(String firstName);
    List<Student> findByFirstNameStartingWith(String firstLetter);
    List<Student> findByLastNameStartingWith(String firstLetter);

    List<Student> findByLastNameIgnoreCase(String lastName);

    List<Student> findByMiddleNameIgnoreCase(String middleName);

    List<Student> findByFirstNameIgnoreCaseAndLastNameIgnoreCase(String firstName, String lastName);

    List<Student> findByFirstNameIgnoreCaseOrMiddleNameIgnoreCaseOrLastNameIgnoreCase(String firstName, String middleName, String lastName);

    @Query("SELECT s FROM Student s WHERE s.email LIKE %:keyword% OR s.firstName LIKE %:keyword% OR s.lastName LIKE %:keyword%")
    List<Student> searchByKeyword(@Param("keyword") String keyword);

    Optional<Student> findByEmail(String email);

    @Query(value = "SELECT * FROM student WHERE EXTRACT(MONTH FROM dob) = :month", nativeQuery = true)
    List<Student> findByBirthMonth(@Param("month") int month);

    List<Student> findByDob(LocalDate dob);

    List<Student> findByDobBefore(LocalDate date);

    List<Student> findByDobAfter(LocalDate date);

    List<Student> findBySex(Character sex);

    List<Student> findByDobBetween(LocalDate startDate, LocalDate endDate);

    List<Student> findByLastNameOrderByFirstNameAsc(String lastName);

    long countBySex(Character sex);

    long countByDob(LocalDate dob);

    List<Student> findBySexOrderByLastNameAsc(Character sex);

    List<Student> findByEmailContainingIgnoreCase(String emailFragment);

    List<Student> findByGradeLevelGradeLevelNameContains(String gradeLevelName);


}
