package main

import (
	tea "github.com/charmbracelet/bubbletea"
	"log"
	"saaj/input"
)

func login() {
	questions := []input.Question{
		input.NewShortQuestion("please enter your username:", "username"),
		input.NewShortQuestion("please enter your password:", "password"),
	}
	main := input.NewParallelQuestion(questions)

	p := tea.NewProgram(*main, tea.WithAltScreen())
	if _, err := p.Run(); err != nil {
		log.Fatal(err)
	}
}