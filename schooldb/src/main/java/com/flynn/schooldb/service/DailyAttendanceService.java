package com.flynn.schooldb.service;
import com.flynn.schooldb.entity.AttendanceType;
import com.flynn.schooldb.entity.DailyAttendance;
import com.flynn.schooldb.entity.Student;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

public interface DailyAttendanceService {
    List<DailyAttendance> findByStudentId(Long studentId);
    List<DailyAttendance> findByDate(LocalDate date);
    List<DailyAttendance> findByStudentIdAndDate(Long studentId, LocalDate date);
    List<DailyAttendance> findByExcuseNoteNotNull();
    List<DailyAttendance> findByAttendanceTypeName(@Param("attendanceTypeName") String attendanceTypeName);
    List<DailyAttendance> findByStudentIdAndDateAndAttendanceTypeName(@Param("studentId") Long studentId, @Param("date") LocalDate date, @Param("attendanceTypeName") String attendanceTypeName);

}
