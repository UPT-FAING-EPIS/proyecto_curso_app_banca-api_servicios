using Microsoft.AspNetCore.Mvc;
using MySql.Data.MySqlClient;
using Clientes.Negocio;



namespace Clientes.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ClienteController : ControllerBase
    {

        private readonly ILogger<ClienteController> _logger;
        private readonly MySqlConnection connection;


        public ClienteController(ILogger<ClienteController> logger)
        {
            _logger = logger;
            this.connection = new Conexion().ObtenerConexion();

        }


        [HttpGet]
        public IEnumerable<Cliente> Get()
        {
            List<Cliente> clientes = new List<Cliente>();
            

            using (var command = new MySqlCommand("SELECT * FROM Clientes", connection))
            {
                connection.Open();

                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        var cliente = new Cliente
                        {
                            IdCliente = reader.GetInt32("IdCliente"),
                            NombreCliente = reader.GetString("NombreCliente"),
                            Direccion = reader.GetString("Direccion"),
                            Pais = reader.GetString("Pais"),
                            CodigoPostal = reader.GetString("CodigoPostal"),
                            NumeroTelefono = reader.GetString("NumeroTelefono"),
                            CorreoElectronico = reader.GetString("CorreoElectronico"),
                            EstadoCuenta = reader.GetString("EstadoCuenta")
                        };

                        clientes.Add(cliente);
                    }
                }

                connection.Close();
            }

            return clientes;

        }

        [HttpPost]
        public IActionResult Post([FromBody] Cliente cliente)
        {
            try
            {
                using (var command = new MySqlCommand("INSERT INTO Clientes (NombreCliente, Direccion, Pais, CodigoPostal, NumeroTelefono, CorreoElectronico, EstadoCuenta) VALUES (@NombreCliente, @Direccion, @Pais, @CodigoPostal, @NumeroTelefono, @CorreoElectronico, @EstadoCuenta)", connection))
                {
                    command.Parameters.AddWithValue("@NombreCliente", cliente.NombreCliente);
                    command.Parameters.AddWithValue("@Direccion", cliente.Direccion);
                    command.Parameters.AddWithValue("@Pais", cliente.Pais);
                    command.Parameters.AddWithValue("@CodigoPostal", cliente.CodigoPostal);
                    command.Parameters.AddWithValue("@NumeroTelefono", cliente.NumeroTelefono);
                    command.Parameters.AddWithValue("@CorreoElectronico", cliente.CorreoElectronico);
                    command.Parameters.AddWithValue("@EstadoCuenta", cliente.EstadoCuenta);

                    connection.Open();
                    command.ExecuteNonQuery();
                    connection.Close();
                }

                return Ok();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error al guardar el cliente en la base de datos.");
                return StatusCode(500, "Error interno del servidor.");
            }
        }


        [HttpPut("{id}")]
        public IActionResult Put(int id, [FromBody] Cliente cliente)
        {
            try
            {
                using (var command = new MySqlCommand("UPDATE Clientes SET NombreCliente = @NombreCliente, Direccion = @Direccion, Pais = @Pais, CodigoPostal = @CodigoPostal, NumeroTelefono = @NumeroTelefono, CorreoElectronico = @CorreoElectronico, EstadoCuenta = @EstadoCuenta WHERE IdCliente = @IdCliente", connection))
                {
                    command.Parameters.AddWithValue("@NombreCliente", cliente.NombreCliente);
                    command.Parameters.AddWithValue("@Direccion", cliente.Direccion);
                    command.Parameters.AddWithValue("@Pais", cliente.Pais);
                    command.Parameters.AddWithValue("@CodigoPostal", cliente.CodigoPostal);
                    command.Parameters.AddWithValue("@NumeroTelefono", cliente.NumeroTelefono);
                    command.Parameters.AddWithValue("@CorreoElectronico", cliente.CorreoElectronico);
                    command.Parameters.AddWithValue("@EstadoCuenta", cliente.EstadoCuenta);
                    command.Parameters.AddWithValue("@IdCliente", id);

                    connection.Open();
                    int rowsAffected = command.ExecuteNonQuery();
                    connection.Close();

                    if (rowsAffected > 0)
                        return Ok();
                    else
                        return NotFound();
                }
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error al actualizar el cliente en la base de datos.");
                return StatusCode(500, "Error interno del servidor.");
            }
        }






    }
}