package com.dmgroup.springboot.pojo;

import java.io.Serializable;
import java.util.List;

public class Route implements Serializable{


	private static final long serialVersionUID = 1L;
	private String BRAND;
	private List<String> STATIONS_NAME_LIST;
	private List<Integer> STATIONS_ID_LIST;
	private List<Integer> FIBERS_ID_LIST;
	public String getBRAND() {
		return BRAND;
	}
	public void setBRAND(String bRAND) {
		BRAND = bRAND;
	}
	public List<String> getSTATIONS_NAME_LIST() {
		return STATIONS_NAME_LIST;
	}
	public void setSTATIONS_NAME_LIST(List<String> sTATIONS_NAME_LIST) {
		STATIONS_NAME_LIST = sTATIONS_NAME_LIST;
	}
	public List<Integer> getSTATIONS_ID_LIST() {
		return STATIONS_ID_LIST;
	}
	public void setSTATIONS_ID_LIST(List<Integer> sTATIONS_ID_LIST) {
		STATIONS_ID_LIST = sTATIONS_ID_LIST;
	}
	public List<Integer> getFIBERS_ID_LIST() {
		return FIBERS_ID_LIST;
	}
	public void setFIBERS_ID_LIST(List<Integer> fIBERS_ID_LIST) {
		FIBERS_ID_LIST = fIBERS_ID_LIST;
	}
	public static long getSerialversionuid() {
		return serialVersionUID;
	}
}
