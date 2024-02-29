package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.DailyAttendance;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.util.List;

@Repository
public interface DailyAttendanceRepository extends JpaRepository<DailyAttendance, Long> {
    @Query("SELECT da FROM DailyAttendance da WHERE da.student.studentId = :studentId")
    List<DailyAttendance> findByStudentId(Long studentId);
    List<DailyAttendance> findByDate(LocalDate date);
    @Query("SELECT da FROM DailyAttendance da WHERE da.student.id = :studentId AND da.date = :date")
    List<DailyAttendance> findByStudentIdAndDate(Long studentId, LocalDate date);
    List<DailyAttendance> findByExcuseNoteNotNull();
    @Query("SELECT da FROM DailyAttendance da JOIN da.attendanceType at WHERE at.attendanceType = :attendanceTypeName")
    List<DailyAttendance> findByAttendanceTypeName(@Param("attendanceTypeName") String attendanceTypeName);
    @Query("SELECT da FROM DailyAttendance da JOIN da.attendanceType at WHERE da.student.studentId = :studentId AND da.date = :date AND at.attendanceType = :attendanceTypeName")
    List<DailyAttendance> findByStudentIdAndDateAndAttendanceTypeName(@Param("studentId") Long studentId, @Param("date") LocalDate date, @Param("attendanceTypeName") String attendanceTypeName);

}
