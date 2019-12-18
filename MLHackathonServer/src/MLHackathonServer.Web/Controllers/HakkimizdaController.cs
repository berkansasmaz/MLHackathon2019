using Microsoft.AspNetCore.Mvc;

namespace MLHackathonServer.Web.Controllers
{
    public class HakkimizdaController : Controller
    {
    	public IActionResult Index()
       {
            return View();
        }
    }
}