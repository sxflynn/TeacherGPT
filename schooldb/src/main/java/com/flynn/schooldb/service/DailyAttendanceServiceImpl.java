package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.DailyAttendance;
import com.flynn.schooldb.repository.DailyAttendanceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.List;
import java.util.stream.Collectors;

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
        return convertAttendanceToEST(dailyAttendanceRepository.findByStudentStudentId(studentId));
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByDate(LocalDate date) {
        return convertAttendanceToEST(dailyAttendanceRepository.findByDate(date));
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByStudentStudentIdAndDate(Long studentId, LocalDate date) {
        return convertAttendanceToEST(dailyAttendanceRepository.findByStudentStudentIdAndDate(studentId,date));
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByExcuseNoteNotNull() {
        return convertAttendanceToEST(dailyAttendanceRepository.findByExcuseNoteNotNull());
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByStudentStudentIdAndAttendanceTypeAttendanceType(Long studentId, String attendanceTypeName) {
        return convertAttendanceToEST(dailyAttendanceRepository.findByStudentStudentIdAndAttendanceTypeAttendanceType(studentId,attendanceTypeName));
    }

    @Override
    public List<DailyAttendance> findByStudentStudentIdAndNotFullAttendance(Long studentId) {
        String attendanceTypeName = "Full Attendance";
        return convertAttendanceToEST(dailyAttendanceRepository.findByStudentStudentIdAndAttendanceTypeAttendanceTypeNot(studentId,attendanceTypeName));
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByAttendanceTypeAttendanceTypeAndDate(String attendanceTypeName, LocalDate date) {
        return convertAttendanceToEST(dailyAttendanceRepository.findByAttendanceTypeAttendanceTypeAndDate(attendanceTypeName,date));
    }

    private List<DailyAttendance> convertAttendanceToEST(List<DailyAttendance> attendances){
        return attendances.stream()
                .map(this::convertTimesForAttendance)
                .collect(Collectors.toList());
    }

    private DailyAttendance convertTimesForAttendance(DailyAttendance attendance) {
        if (attendance.getArrival() != null) {
            ZonedDateTime estArrival = attendance.getArrival().atZoneSameInstant(ZoneId.of("America/New_York"));
            attendance.setArrival(estArrival.toOffsetDateTime());
        }
        if (attendance.getDeparture() != null) {
            ZonedDateTime estDeparture = attendance.getDeparture().atZoneSameInstant(ZoneId.of("America/New_York"));
            attendance.setDeparture(estDeparture.toOffsetDateTime());
        }
        return attendance;
    }
}
