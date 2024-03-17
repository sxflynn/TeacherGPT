package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.DailyAttendance;
import org.springframework.cglib.core.Local;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.util.List;

@Repository
public interface DailyAttendanceRepository extends JpaRepository<DailyAttendance, Long> {

    List<DailyAttendance> findByStudentStudentId(Long studentId);
    List<DailyAttendance> findByDate(LocalDate date);
    List<DailyAttendance> findByStudentStudentIdAndDate(Long studentId, LocalDate date);
    List<DailyAttendance> findByExcuseNoteNotNull();
    List<DailyAttendance> findByStudentStudentIdAndAttendanceTypeAttendanceType(Long studentId, String attendanceTypeName);
    List<DailyAttendance> findByStudentStudentIdAndAttendanceTypeAttendanceTypeNot(Long studentId, String attendanceTypeName);
    List<DailyAttendance> findByAttendanceTypeAttendanceTypeAndDate(String attendanceTypeName, LocalDate date);
    long countByStudentStudentIdAndAttendanceTypeAttendanceType(Long studentId, String attendanceTypeName);
    long countByStudentStudentIdAndAttendanceTypeAttendanceTypeAndDateBetween(long studentId, String attendanceTypeName, LocalDate startDate, LocalDate endDate);
    long countByStudentStudentIdAndDateBetween(Long studentId, LocalDate startDate, LocalDate endDate);
    long countByDateBetween(LocalDate startDate, LocalDate endDate);
    long countByAttendanceTypeAttendanceTypeAndDateBetween(String attendanceTypeName, LocalDate startDate, LocalDate endDate);
    long countByStudentStudentId(Long studentId);
    long countByAttendanceTypeAttendanceType(String attendanceTypeName);

}
