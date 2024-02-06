package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.DailyAttendance;
import com.flynn.schooldb.entity.Student;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDate;
import java.util.List;

public interface DailyAttendanceRepository extends JpaRepository<DailyAttendance, Long> {
    List<DailyAttendance> findByStudent(Student student);
    List<DailyAttendance> findByDate(LocalDate date);
    List<DailyAttendance> findByStudentAndDate(Student student, LocalDate date);
    List<DailyAttendance> findByExcuseNoteNotNull();
}
