using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace MLHackathonServer.Web.Controllers
{
    public class HakkimizdaController : Controller
    {
		[Authorize(Roles="Sektor")]
    	public IActionResult Index()
       {
            return View();
        }
    }
}