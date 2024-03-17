package com.flynn.schooldb.service;

import com.flynn.schooldb.dto.AttendanceSummaryDTO;
import com.flynn.schooldb.entity.DailyAttendance;
import java.time.LocalDate;
import java.util.List;

public interface DailyAttendanceService {
    List<DailyAttendance> findByStudentStudentId(Long studentId);
    List<DailyAttendance> findByDate(LocalDate date);
    List<DailyAttendance> findByStudentStudentIdAndDate(Long studentId, LocalDate date);
    List<DailyAttendance> findByExcuseNoteNotNull();
    List<DailyAttendance> findByStudentStudentIdAndAttendanceTypeAttendanceType(Long studentId, String attendanceTypeName);
    List<DailyAttendance> findByStudentStudentIdAndNotFullAttendance(Long studentId);
    List<DailyAttendance> findByAttendanceTypeAttendanceTypeAndDate(String attendanceTypeName, LocalDate date);
    AttendanceSummaryDTO summarizeStudentAttendance(Long studentId);
    AttendanceSummaryDTO summarizeStudentAttendanceBetweenDates(Long studentId, LocalDate startDate, LocalDate endDate);
    AttendanceSummaryDTO summarizeSchoolAttendance();
    AttendanceSummaryDTO summarizeSchoolAttendanceBetweenDates(LocalDate startDate, LocalDate endDate);

}
