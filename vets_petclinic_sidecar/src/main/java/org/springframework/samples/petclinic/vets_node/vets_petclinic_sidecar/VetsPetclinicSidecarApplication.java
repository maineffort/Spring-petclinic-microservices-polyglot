package org.springframework.samples.petclinic.vets_node.vets_petclinic_sidecar;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.sidecar.EnableSidecar;

@SpringBootApplication
@EnableSidecar
public class VetsPetclinicSidecarApplication {

	public static void main(String[] args) {
		SpringApplication.run(VetsPetclinicSidecarApplication.class, args);
	}
}
