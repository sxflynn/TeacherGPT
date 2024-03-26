package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.Staff;
import com.flynn.schooldb.repository.StaffRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.Set;

@Service
public class StaffServiceImpl implements StaffService{

    private final StaffRepository staffRepository;

    @Autowired
    public StaffServiceImpl(StaffRepository staffRepository) {
        this.staffRepository = staffRepository;
    }

    @Override
    public Optional<Staff> staffFindById(Long id) {
        return staffRepository.findById(id);
    }

    @Override
    public List<Staff> staffListAllStaff() {
        return staffRepository.findAll();
    }

    @Override
    public Set<Staff> staffSearchByKeyword(String keyword) {
        return staffRepository.searchByKeyword(keyword);
    }

    @Override
    public Set<Staff> staffFindByLastName(String lastName) {
        return staffRepository.findByLastNameIgnoreCase(lastName);
    }

    @Override
    public Set<Staff> staffFindByFirstName(String firstName) {
        return staffRepository.findByFirstNameIgnoreCase(firstName);
    }

    @Override
    public Set<Staff> staffFindByMiddleName(String middleName) {
        return staffRepository.findByMiddleNameIgnoreCase(middleName);
    }

    @Override
    public Set<Staff> staffFindByEmail(String email) {
        return staffRepository.findByEmailIgnoreCase(email);
    }

    @Override
    public Set<Staff> staffFindByPositionContains(String position) {
        return staffRepository.findByPositionContains(position);
    }

    @Override
    public Set<Staff> staffFindByGradeLevelName(String name) {
        return staffRepository.findByStaffGradeLevelsGradeLevelGradeLevelNameContains(name);
    }
}
