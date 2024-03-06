package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.DailyAttendance;
import com.flynn.schooldb.repository.DailyAttendanceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.util.List;

@Service
public class DailyAttendanceServiceImpl implements DailyAttendanceService {

    private final DailyAttendanceRepository dailyAttendanceRepository;

    @Autowired
    public DailyAttendanceServiceImpl(DailyAttendanceRepository dailyAttendanceRepository) {
        this.dailyAttendanceRepository = dailyAttendanceRepository;
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByStudentStudentId(Long studentId) {
        return dailyAttendanceRepository.findByStudentStudentId(studentId);
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByDate(LocalDate date) {
        return dailyAttendanceRepository.findByDate(date);
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByStudentStudentIdAndDate(Long studentId, LocalDate date) {
        return dailyAttendanceRepository.findByStudentStudentIdAndDate(studentId,date);
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByExcuseNoteNotNull() {
        return dailyAttendanceRepository.findByExcuseNoteNotNull();
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByStudentStudentIdAndAttendanceTypeAttendanceType(Long studentId, String attendanceTypeName) {
        return dailyAttendanceRepository.findByStudentStudentIdAndAttendanceTypeAttendanceType(studentId,attendanceTypeName);
    }

    @Override
    public List<DailyAttendance> findByStudentStudentIdAndNotFullAttendance(Long studentId) {
        String attendanceTypeName = "Full Attendance";
        return dailyAttendanceRepository.findByStudentStudentIdAndAttendanceTypeAttendanceTypeNot(studentId,attendanceTypeName);
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByAttendanceTypeAttendanceTypeAndDate(String attendanceTypeName, LocalDate date) {
        return dailyAttendanceRepository.findByAttendanceTypeAttendanceTypeAndDate(attendanceTypeName,date);
    }
}
