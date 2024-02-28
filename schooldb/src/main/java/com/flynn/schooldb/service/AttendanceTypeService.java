package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.AttendanceType;

import java.util.List;

public interface AttendanceTypeService{

    List<AttendanceType> findAll();

}
