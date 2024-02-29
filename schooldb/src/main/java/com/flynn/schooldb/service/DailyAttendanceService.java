package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.DailyAttendance;
import java.time.LocalDate;
import java.util.List;

public interface DailyAttendanceService {
    List<DailyAttendance> findByStudentId(Long studentId);
    List<DailyAttendance> findByDate(LocalDate date);
    List<DailyAttendance> findByStudentIdAndDate(Long studentId, LocalDate date);
    List<DailyAttendance> findByExcuseNoteNotNull();
    List<DailyAttendance> findByAttendanceTypeName(String attendanceTypeName);
    List<DailyAttendance> findByStudentIdAndDateAndAttendanceTypeName(Long studentId, LocalDate date, String attendanceTypeName);

}
