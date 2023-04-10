package com.app.entities;

import java.time.LocalDateTime;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Lob;

@Entity
public class Chat {
	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	int chatId;
	int userId;
	@Column(columnDefinition = "longtext")
	String userMessage;
	@Column(columnDefinition="longtext")

	String sakhaResponse;
	LocalDateTime chatDate;
	public int getChatId() {
		return chatId;
	}
	public int getUserId() {
		return userId;
	}
	public String getUserMessage() {
		return userMessage;
	}
	public String getSakhaResponse() {
		return sakhaResponse;
	}
	public LocalDateTime getChatDate() {
		return chatDate;
	}
	public void setChatId(int chatId) {
		this.chatId = chatId;
	}
	public void setUserId(int userId) {
		this.userId = userId;
	}
	public void setUserMessage(String userMessage) {
		this.userMessage = userMessage;
	}
	public void setSakhaResponse(String sakhaResponse) {
		this.sakhaResponse = sakhaResponse;
	}
	public void setChatDate(LocalDateTime chatDate) {
		this.chatDate = chatDate;
	}
	
}
