package com.flynn.schooldb.config;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class CorsConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**") // Maps to all paths
                .allowedOriginPatterns("*")
                .allowedMethods("*") // Allows all methods
                .allowedHeaders("*") // Allows all headers
                .allowCredentials(true); // Allows credentials
    }
}

