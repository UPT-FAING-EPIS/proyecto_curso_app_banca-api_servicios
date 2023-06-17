using MySql.Data.MySqlClient;

namespace Clientes.Negocio
{
    public class Conexion
    {
        private readonly string connectionString;

        string server = "localhost";
        string database = "clientesbanca";
        string username = "root";
        string password = "";



        public Conexion()
        {
            connectionString = $"Server={this.server};Database={this.database};Uid={this.username};Pwd={this.password};";
        }

        public MySqlConnection ObtenerConexion()
        {
            return new MySqlConnection(connectionString);
        }

    }
}
