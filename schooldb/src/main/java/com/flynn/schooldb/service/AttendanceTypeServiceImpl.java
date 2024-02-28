package com.flynn.schooldb.service;


import com.flynn.schooldb.entity.AttendanceType;
import com.flynn.schooldb.repository.AttendanceTypeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AttendanceTypeServiceImpl implements AttendanceTypeService {

    private final AttendanceTypeRepository attendanceTypeRepository;

    @Autowired
    public AttendanceTypeServiceImpl(AttendanceTypeRepository attendanceTypeRepository) {
        this.attendanceTypeRepository = attendanceTypeRepository;
    }

    @Override
    public List<AttendanceType> findAll() {
        return attendanceTypeRepository.findAll();
    }
}
