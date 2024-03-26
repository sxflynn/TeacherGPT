package com.flynn.schooldb.service;
import com.flynn.schooldb.entity.Staff;

import java.util.List;
import java.util.Set;

public interface StaffService {

    List<Staff> staffListAllStaff();

    Set<Staff> staffSearchByKeyword(String keyword);

    Set<Staff> staffFindByLastName(String lastName);

    Set<Staff> staffFindByFirstName(String firstName);

    Set<Staff> staffFindByMiddleName(String middleName);

    Set<Staff> staffFindByEmail(String email);

    Set<Staff> staffFindByPositionContains(String position);

    Set<Staff> staffFindByGradeLevelName(String name);

}
