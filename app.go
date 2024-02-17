package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"html/template"
	"strings"

	// "io"
	"log"
	"net/http"

	"github.com/alecthomas/chroma/quick"

	// "os"
	// "path/filepath"
	// "strconv"
	// "time"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

// App represents the application
type App struct {
	Router *mux.Router
	DB     *sql.DB
}

// New creates a new instance of App
func (app *App) Initialize(Dbuser string, Dbpassword string, Dbname string) error {
	connectionString := fmt.Sprintf("%v:%v@tcp(127.0.0.1:3306)/%v", Dbuser, Dbpassword, Dbname)
	var err error
	app.DB, err = sql.Open("mysql", connectionString)
	if err != nil {
		return err
	}

	app.Router = mux.NewRouter().StrictSlash(true)
	app.handleRoutes()
	return nil
}

// SetDB sets the database connection
func (app *App) Run(address string) {
	log.Fatal(http.ListenAndServe(address, app.Router))
}

func sendResponse(w http.ResponseWriter, statusCode int, payload interface{}, htmlfilename string, contentype string) {
	response, _ := json.Marshal(payload)
	if htmlfilename != "" {
		response = nil
		tmpl, err := template.ParseFiles(htmlfilename)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		err = tmpl.Execute(w, payload)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
	}
	w.Header().Set("Content-type", contentype)
	w.WriteHeader(statusCode)
	if response != nil {
		w.Write(response)

	}
}

func sendError(w http.ResponseWriter, statusCode int, err string) {
	errormessage := map[string]string{"error": err}
	sendResponse(w, statusCode, errormessage, "", "text/html; charset=UTF-8")
}

func (app *App) Home(w http.ResponseWriter, r *http.Request) {
	code := r.FormValue("code")
	langname := r.FormValue("langname")
	theme := r.FormValue("theme")
	data := CodeData{LangName: langname, Width: "12px", Height: "12px", Code: code, Theme: theme}
	errs := quick.Highlight(w, data.Code, data.LangName, "html", data.Theme)
	data.LangName = strings.ToUpper(langname)
	sendResponse(w, http.StatusOK, data, "templates/index.html", "text/html; charset=UTF-8")
	if errs != nil {
		sendError(w, http.StatusInternalServerError, "Failed to highlight code")
		return
	}

}

func (app *App) Chroma(w http.ResponseWriter, r *http.Request) {
	code := r.FormValue("code")
	langname := r.FormValue("langname")
	theme := r.FormValue("theme")
	data := CodeData{LangName: langname, Width: "12px", Height: "12px", Code: code, Theme: theme}
	sendResponse(w, http.StatusOK, data, "templates/chroma.html", "text/html; charset=UTF-8")
}

func (app *App) download(w http.ResponseWriter, r *http.Request) {
	sendResponse(w, http.StatusOK, nil, "templates/download.html", "text/html; charset=UTF-8")
}

func (app *App) handleRoutes() {
	app.Router.HandleFunc("/home", app.Home).Methods("GET")
	app.Router.HandleFunc("/Chroma", app.Chroma).Methods("GET")
	app.Router.HandleFunc("/download", app.download).Methods("GET")
}
