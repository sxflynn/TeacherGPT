package com.flynn.schooldb.graphql.resolver;

import com.flynn.schooldb.entity.DailyAttendance;
import com.flynn.schooldb.service.DailyAttendanceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.time.LocalDate;
import java.util.List;

@Controller
public class DailyAttendanceQueryResolver {
    @Autowired
    private DailyAttendanceService dailyAttendanceService;

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByStudentId(@Argument Long studentId) {
        return dailyAttendanceService.findByStudentId(studentId);
    }

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByDate(@Argument LocalDate date) {
        return dailyAttendanceService.findByDate(date);
    }

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByStudentIdAndDate(@Argument Long studentId, LocalDate date) {
        return dailyAttendanceService.findByStudentIdAndDate(studentId, date);
    }

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByExcuseNoteNotNull() {
        return dailyAttendanceService.findByExcuseNoteNotNull();
    }

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByAttendanceTypeName(@Argument String attendanceTypeName){
        return dailyAttendanceService.findByAttendanceTypeName(attendanceTypeName);
    }

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByStudentIdAndDateAndAttendanceTypeName(@Argument Long studentId, LocalDate date, String attendanceTypeName){
        return dailyAttendanceService.findByStudentIdAndDateAndAttendanceTypeName(studentId,date,attendanceTypeName);
    }

}



