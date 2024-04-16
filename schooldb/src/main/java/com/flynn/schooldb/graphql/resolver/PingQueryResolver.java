package com.flynn.schooldb.graphql.resolver;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;


@Controller
public class PingQueryResolver {

    @QueryMapping
    public String ping() {
        return "Healthy";
    }
}
