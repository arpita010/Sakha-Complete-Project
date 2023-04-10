package com.app.entities;

public class SakhaRequest {

	String userInput;
	String prevMessage;
	public String getUserInput() {
		return userInput;
	}
	public String getPrevMessage() {
		return prevMessage;
	}
	public void setUserInput(String userInput) {
		this.userInput = userInput;
	}
	public void setPrevMessage(String prevMessage) {
		this.prevMessage = prevMessage;
	}
	@Override
	public String toString() {
		return "SakhaRequest [userInput=" + userInput + ", prevMessage=" + prevMessage + "]";
	}
	
	
}
