package com.flynn.schooldb.graphql.resolver;

import com.flynn.schooldb.entity.AttendanceType;
import com.flynn.schooldb.service.AttendanceTypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.util.List;

@Controller
public class AttendanceTypeQueryResolver {
    @Autowired
    private AttendanceTypeService attendanceTypeService;

    @QueryMapping
    public List<AttendanceType> attendanceTypefindAll() {
        return attendanceTypeService.findAll();
    }

}
