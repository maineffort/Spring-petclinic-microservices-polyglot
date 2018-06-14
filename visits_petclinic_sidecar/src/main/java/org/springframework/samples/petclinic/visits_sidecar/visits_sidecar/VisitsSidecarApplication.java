package org.springframework.samples.petclinic.visits_sidecar.visits_sidecar;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.sidecar.EnableSidecar;

@SpringBootApplication
@EnableSidecar

public class VisitsSidecarApplication {

	public static void main(String[] args) {
		SpringApplication.run(VisitsSidecarApplication.class, args);
	}
}
