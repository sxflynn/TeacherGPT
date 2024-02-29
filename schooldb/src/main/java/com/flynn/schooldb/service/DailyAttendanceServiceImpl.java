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
    public List<DailyAttendance> findByStudentId(Long studentId) {
        return dailyAttendanceRepository.findByStudentId(studentId);
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByDate(LocalDate date) {
        return dailyAttendanceRepository.findByDate(date);
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByStudentIdAndDate(Long studentId, LocalDate date) {
        return dailyAttendanceRepository.findByStudentIdAndDate(studentId,date);
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByExcuseNoteNotNull() {
        return dailyAttendanceRepository.findByExcuseNoteNotNull();
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByAttendanceTypeName(String attendanceTypeName) {
        return dailyAttendanceRepository.findByAttendanceTypeName(attendanceTypeName);
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByStudentIdAndDateAndAttendanceTypeName(Long studentId, LocalDate date, String attendanceTypeName) {
        return dailyAttendanceRepository.findByStudentIdAndDateAndAttendanceTypeName(studentId,date,attendanceTypeName);
    }
}
