package com.flynn.schooldb.service;

import com.flynn.schooldb.dto.AttendanceSummaryDTO;
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
        return convertAttendanceToEST(dailyAttendanceRepository.findByStudentStudentIdAndDate(studentId, date));
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByExcuseNoteNotNull() {
        return convertAttendanceToEST(dailyAttendanceRepository.findByExcuseNoteNotNull());
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByStudentStudentIdAndAttendanceTypeAttendanceType(Long studentId, String attendanceTypeName) {
        return convertAttendanceToEST(dailyAttendanceRepository.findByStudentStudentIdAndAttendanceTypeAttendanceType(studentId, attendanceTypeName));
    }

    @Override
    public List<DailyAttendance> findByStudentStudentIdAndNotFullAttendance(Long studentId) {
        String attendanceTypeName = "Full Attendance";
        return convertAttendanceToEST(dailyAttendanceRepository.findByStudentStudentIdAndAttendanceTypeAttendanceTypeNot(studentId, attendanceTypeName));
    }

    @Override
    @Transactional(readOnly = true)
    public List<DailyAttendance> findByAttendanceTypeAttendanceTypeAndDate(String attendanceTypeName, LocalDate date) {
        return convertAttendanceToEST(dailyAttendanceRepository.findByAttendanceTypeAttendanceTypeAndDate(attendanceTypeName, date));
    }

    @Override
    public AttendanceSummaryDTO summarizeStudentAttendance(Long studentId) {
        long totalDays = dailyAttendanceRepository.countByStudentStudentId(studentId);
        long daysFullAttendance = dailyAttendanceRepository.countByStudentStudentIdAndAttendanceTypeAttendanceType(studentId, "Full Attendance");
        long daysPartialExcusedAbsence = dailyAttendanceRepository.countByStudentStudentIdAndAttendanceTypeAttendanceType(studentId, "Partial Excused Absence");
        long daysPartialUnexcusedAbsence = dailyAttendanceRepository.countByStudentStudentIdAndAttendanceTypeAttendanceType(studentId, "Partial Unexcused Absence");
        long daysUnexcusedAbsence = dailyAttendanceRepository.countByStudentStudentIdAndAttendanceTypeAttendanceType(studentId, "Unexcused Absence");
        long daysExcusedAbsence = dailyAttendanceRepository.countByStudentStudentIdAndAttendanceTypeAttendanceType(studentId, "Excused Absence");
        double attendanceRate = calculateAttendanceRate(totalDays, daysFullAttendance, (daysPartialExcusedAbsence + daysPartialUnexcusedAbsence), (daysExcusedAbsence + daysUnexcusedAbsence));

        AttendanceSummaryDTO summary = new AttendanceSummaryDTO(
                totalDays,
                daysFullAttendance,
                daysPartialExcusedAbsence,
                daysPartialUnexcusedAbsence,
                daysUnexcusedAbsence,
                daysExcusedAbsence,
                attendanceRate
        );

        return summary;
    }

    @Override
    public AttendanceSummaryDTO summarizeSchoolAttendance() {
        long totalDays = dailyAttendanceRepository.count();
        long daysFullAttendance = dailyAttendanceRepository.countByAttendanceTypeAttendanceType("Full Attendance");
        long daysPartialExcusedAbsence = dailyAttendanceRepository.countByAttendanceTypeAttendanceType("Partial Excused Absence");
        long daysPartialUnexcusedAbsence = dailyAttendanceRepository.countByAttendanceTypeAttendanceType("Partial Unexcused Absence");
        long daysUnexcusedAbsence = dailyAttendanceRepository.countByAttendanceTypeAttendanceType("Unexcused Absence");
        long daysExcusedAbsence = dailyAttendanceRepository.countByAttendanceTypeAttendanceType("Excused Absence");
        double attendanceRate = calculateAttendanceRate(totalDays, daysFullAttendance, (daysPartialExcusedAbsence + daysPartialUnexcusedAbsence), (daysExcusedAbsence + daysUnexcusedAbsence));

        AttendanceSummaryDTO summary = new AttendanceSummaryDTO(
                totalDays,
                daysFullAttendance,
                daysPartialExcusedAbsence,
                daysPartialUnexcusedAbsence,
                daysUnexcusedAbsence,
                daysExcusedAbsence,
                attendanceRate
        );

        return summary;

    }

    @Override
    public AttendanceSummaryDTO summarizeStudentAttendanceBetweenDates(Long studentId, LocalDate startDate, LocalDate endDate) {
        long totalDays = dailyAttendanceRepository.countByStudentStudentIdAndDateBetween(studentId, startDate, endDate);
        long daysFullAttendance = dailyAttendanceRepository.countByStudentStudentIdAndAttendanceTypeAttendanceTypeAndDateBetween(studentId, "Full Attendance", startDate, endDate);
        long daysPartialExcusedAbsence = dailyAttendanceRepository.countByStudentStudentIdAndAttendanceTypeAttendanceTypeAndDateBetween(studentId, "Partial Excused Absence", startDate, endDate);
        long daysPartialUnexcusedAbsence = dailyAttendanceRepository.countByStudentStudentIdAndAttendanceTypeAttendanceTypeAndDateBetween(studentId, "Partial Unexcused Absence", startDate, endDate);
        long daysUnexcusedAbsence = dailyAttendanceRepository.countByStudentStudentIdAndAttendanceTypeAttendanceTypeAndDateBetween(studentId, "Unexcused Absence", startDate, endDate);
        long daysExcusedAbsence = dailyAttendanceRepository.countByStudentStudentIdAndAttendanceTypeAttendanceTypeAndDateBetween(studentId, "Excused Absence", startDate, endDate);
        double attendanceRate = calculateAttendanceRate(totalDays, daysFullAttendance, (daysPartialExcusedAbsence + daysPartialUnexcusedAbsence), (daysExcusedAbsence + daysUnexcusedAbsence));

        AttendanceSummaryDTO summary = new AttendanceSummaryDTO(
                totalDays,
                daysFullAttendance,
                daysPartialExcusedAbsence,
                daysPartialUnexcusedAbsence,
                daysUnexcusedAbsence,
                daysExcusedAbsence,
                attendanceRate
        );

        return summary;
    }

    @Override
    public AttendanceSummaryDTO summarizeSchoolAttendanceBetweenDates(LocalDate startDate, LocalDate endDate) {
        long totalDays = dailyAttendanceRepository.countByDateBetween(startDate, endDate);
        long daysFullAttendance = dailyAttendanceRepository.countByAttendanceTypeAttendanceTypeAndDateBetween("Full Attendance", startDate, endDate);
        long daysPartialExcusedAbsence = dailyAttendanceRepository.countByAttendanceTypeAttendanceTypeAndDateBetween("Partial Excused Absence", startDate, endDate);
        long daysPartialUnexcusedAbsence = dailyAttendanceRepository.countByAttendanceTypeAttendanceTypeAndDateBetween("Partial Unexcused Absence", startDate, endDate);
        long daysUnexcusedAbsence = dailyAttendanceRepository.countByAttendanceTypeAttendanceTypeAndDateBetween("Unexcused Absence", startDate,endDate);
        long daysExcusedAbsence = dailyAttendanceRepository.countByAttendanceTypeAttendanceTypeAndDateBetween("Excused Absence", startDate, endDate);
        double attendanceRate = calculateAttendanceRate(totalDays, daysFullAttendance, (daysPartialExcusedAbsence + daysPartialUnexcusedAbsence), (daysExcusedAbsence + daysUnexcusedAbsence));

        AttendanceSummaryDTO summary = new AttendanceSummaryDTO(
                totalDays,
                daysFullAttendance,
                daysPartialExcusedAbsence,
                daysPartialUnexcusedAbsence,
                daysUnexcusedAbsence,
                daysExcusedAbsence,
                attendanceRate
        );

        return summary;
    }

    private double calculateAttendanceRate(long totalDays, long fullDays, long partialDays, long absentDays) {
        long fullDaysTotal = fullDays * 1;
        double partialDaysTotal = partialDays * 0.5;
        long absentDaysTotal = absentDays * 0;
        return (fullDaysTotal + partialDaysTotal + absentDaysTotal) / totalDays;
    }

    private List<DailyAttendance> convertAttendanceToEST(List<DailyAttendance> attendances) {
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
