package com.flynn.schooldb.graphql.resolver;

import com.flynn.schooldb.entity.Staff;
import com.flynn.schooldb.service.StaffService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.util.List;
import java.util.Optional;
import java.util.Set;

@Controller
public class StaffQueryResolver {

    @Autowired
    private StaffService staffService;

    @QueryMapping
    public Optional<Staff> staffFindById(@Argument Long id){
        return staffService.staffFindById(id);
    }

    @QueryMapping
    public List<Staff> staffListAllStaff() {
        return staffService.staffListAllStaff();
    }

    @QueryMapping
    public Set<Staff> staffSearchByKeyword(@Argument String keyword) {
        return staffService.staffSearchByKeyword(keyword);
    }

    @QueryMapping
    public Set<Staff> staffFindByLastName(@Argument String lastName) {
        return staffService.staffFindByLastName(lastName);
    }

    @QueryMapping
    public Set<Staff> staffFindByFirstName(@Argument String firstName) {
        return staffService.staffFindByFirstName(firstName);
    }

    @QueryMapping
    public Set<Staff> staffFindByMiddleName(@Argument String middleName) {
        return staffService.staffFindByMiddleName(middleName);
    }

    @QueryMapping
    public Set<Staff> staffFindByEmail(@Argument String email) {
        return staffService.staffFindByEmail(email);
    }

    @QueryMapping
    public Set<Staff> staffFindByPositionContains(@Argument String position) {
        return staffService.staffFindByPositionContains(position);
    }

    @QueryMapping
    public Set<Staff> staffFindByGradeLevelName(@Argument String name) {
        return staffService.staffFindByGradeLevelName(name);
    }

}
