package main
func main() {
	app := App{}
	app.Initialize(Dbuser, Dbpassword, Dbname)
	app.Run("localhost:1892")
}
